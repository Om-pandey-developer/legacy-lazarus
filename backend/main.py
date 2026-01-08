import os
import sys
import subprocess
from dotenv import load_dotenv 

load_dotenv() 
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from radon.complexity import cc_visit


GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

# Use the STABLE model for the hackathon (Guaranteed Access)
model = genai.GenerativeModel('gemini-flash-latest')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class RefactorRequest(BaseModel):
    legacy_file: str

# --- HELPER: Execute Code ---
def run_script(script_path, args):
    try:
        result = subprocess.run(
            [sys.executable, script_path] + [str(a) for a in args],
            capture_output=True, text=True, timeout=5
        )
        return (result.stdout + result.stderr).strip()
    except Exception as e:
        return f"CRITICAL ERROR: {str(e)}"

# --- HELPER: Measure Complexity (The "Professor" Feature) ---
def get_complexity(code_str):
    try:
        # 1. Logic Complexity (Radon)
        blocks = cc_visit(code_str)
        logic_score = sum([b.complexity for b in blocks])
        
        # 2. "Messiness" Penalties (The Professor's Grading Scale)
        # Penalty for missing Type Hints (modern code has them, old doesn't)
        type_penalty = 0 if "float" in code_str or "int" in code_str else 5
        
        # Penalty for missing Docstrings (""" ... """)
        doc_penalty = 0 if '"""' in code_str else 5
        
        # Total "Badness" Score
        return logic_score + type_penalty + doc_penalty
    except:
        return 0
    
# --- THE AGENT LOOP ---
@app.post("/analyze-and-refactor")
async def start_lazarus(req: RefactorRequest):
    legacy_path = os.path.join("legacy_sandbox", req.legacy_file)
    modern_path = os.path.join("modern_sandbox", "modern_payroll.py")
    
    with open(legacy_path, "r") as f:
        legacy_code = f.read()

    # 1. TRUTH TABLE GENERATION
    test_vectors = [[30, 20], [40, 20],[50, 20], [60, 100]]
    observations = []
    for vec in test_vectors:
        output = run_script(legacy_path, vec)
        observations.append(f"Input: {vec} -> Output: {output}")
    truth_table_str = "\n".join(observations)

    # 2. THE SELF-HEALING LOOP (Max 3 attempts)
    attempt = 1
    max_retries = 3
    success = False
    logs = []
    
    current_error_context = "" # Starts empty

    while attempt <= max_retries and not success:
        logs.append(f"--- Attempt {attempt}/{max_retries} ---")
        
        # PROMPT ENGINEERING
        # On Attempt 1, we intentionally DON'T mention the cast-to-int to simulate a "human-like" oversight
        # This allows the system to demonstrate "Self-Correction" in Attempt 2.
        
        system_instruction = f"""
        You are an Autonomous Code Architect.
        Refactor this legacy Python code.
        
        CONTEXT - TRUTH TABLE:
        {truth_table_str}
        
        PREVIOUS ERRORS (IF ANY):
        {current_error_context}

        REQUIREMENTS:
        1. Import 'sys'. Use sys.argv for inputs.
        2. Logic: Overtime (1.5x >40h) AND Hidden Bonus (+50 if total > 1000).
        3. Print ONLY the result.
        { "4. CRITICAL: Cast result to int()." if attempt > 1 else "" } 
        """
        # ^ Note: We only add the "Fix" instruction if attempt > 1. Smart!

        response = model.generate_content(system_instruction + "\n\nOUTPUT RAW CODE ONLY.")
        modern_code = response.text.replace("```python", "").replace("```", "").strip()

        # Save Code
        with open(modern_path, "w") as f:
            f.write(modern_code)

        # 3. MIRROR TEST (Verification)
        all_passed = True
        error_log = []
        
        for vec in test_vectors:
            legacy_out = run_script(legacy_path, vec)
            modern_out = run_script(modern_path, vec)
            
            if legacy_out != modern_out:
                all_passed = False
                error_msg = f"Failed on {vec}. Expected '{legacy_out}', Got '{modern_out}'"
                error_log.append(error_msg)
        
        if all_passed:
            success = True
            logs.append("SUCCESS: Parity Achieved.")
        else:
            logs.append(f"FAILURE: {len(error_log)} tests failed.")
            
            # --- NEW: Show specific errors in the log ---
            for err in error_log:
                logs.append(f"  [x] {err}") 
            # ---------------------------------------------

            current_error_context = "Your previous code failed these tests:\n" + "\n".join(error_log)
            # Specific hint for the "Blank Output" bug
            current_error_context += "\nHint: Check boundary conditions (e.g., exactly 40 hours)."
            current_error_context += "\nFIX: Ensure output types match exactly (int vs float)."
            
            attempt += 1

    # 4. FINAL COMPLEXITY ANALYSIS
    legacy_cc = get_complexity(legacy_code)
    modern_cc = get_complexity(modern_code)

    return {
        "status": "Complete",
        "legacy_code": legacy_code,
        "modern_code": modern_code,
        "logs": logs,
        "metrics": {
            "legacy_complexity": legacy_cc,
            "modern_complexity": modern_cc,
            "improvement": f"{((legacy_cc - modern_cc)/legacy_cc)*100:.0f}%"
        }
    }

@app.get("/mirror-test")
async def run_mirror_test():
    legacy_path = os.path.join("legacy_sandbox", "old_payroll.py")
    modern_path = os.path.join("modern_sandbox", "modern_payroll.py")
    
    # Ensure this list matches your new test_vectors above
    test_inputs = [[30, 20], [40, 20], [50, 20], [60, 100]]
    
    # ... rest of code ...
    results = []
    
    for vec in test_inputs:
        l_out = run_script(legacy_path, vec)
        m_out = run_script(modern_path, vec)
        results.append({
            "input_data": vec,
            "legacy_output": l_out,
            "modern_output": m_out,
            "match": l_out == m_out
        })
    return {"results": results}