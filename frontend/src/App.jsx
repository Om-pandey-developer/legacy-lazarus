import { useState } from 'react'
import './App.css'

function App() {
  const [logs, setLogs] = useState([]);
  const [legacyCode, setLegacyCode] = useState("");
  const [modernCode, setModernCode] = useState("");
  const [testResults, setTestResults] = useState([]);
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(false);
  const delay = (ms) => new Promise(res => setTimeout(res, ms));

  const startLazarus = async () => {
    setLoading(true);
    setLogs([]);
    setTestResults([]);
    setMetrics(null);
    setLegacyCode(""); 
    setModernCode(""); 
    
    // Initial "Boot up" sequence
    setLogs(prev => [...prev, "> Initializing Gemini 3 Environment..."]);
    await delay(800);
    setLogs(prev => [...prev, "> Mounting Legacy Container..."]);
    await delay(800);

    try {
      // 1. CALL BACKEND 
      const res = await fetch("http://127.0.0.1:8000/analyze-and-refactor", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ legacy_file: "old_payroll.py" })
      });
      const data = await res.json();
      
      // 2. SHOW LEGACY CODE FIRST
      setLegacyCode(data.legacy_code);
      setLogs(prev => [...prev, "> Legacy Code Ingested."]);
      await delay(1000);

      
      for (const logLine of data.logs) {
        setLogs(prev => [...prev, logLine]);
        
        
        if (logLine.includes("FAILURE")) {
            await delay(2000); 
        } else if (logLine.includes("Attempt")) {
            await delay(1000); 
        } else {
            await delay(500); 
        }
      }

      // 4. REVEAL MODERN CODE & METRICS
      setModernCode(data.modern_code);
      setMetrics(data.metrics);
      await delay(1000);

      // 5. RUN FINAL MIRROR TEST
      setLogs(prev => [...prev, "> Running Final Verification..."]);
      const verRes = await fetch("http://127.0.0.1:8000/mirror-test");
      const verData = await verRes.json();
      
      setTestResults(verData.results); 

    } catch (e) {
      setLogs(prev => [...prev, "Critical Error: Backend unreachable."]);
    }
    setLoading(false);
  };

  return (
    <div className="app-container">
      <header>
        <h1>Legacy Lazarus <span className="tagline">// Autonomous Refactoring Agent</span></h1>
      </header>
      
      <div className="controls">
        <button className="activate-btn" onClick={startLazarus} disabled={loading}>
          {loading ? "EXECUTING REFACTORING LOOP..." : "ACTIVATE LAZARUS AGENT"}
        </button>
        
        {/*  METRICS DASHBOARD */}
        {metrics && (
          <div className="metrics-panel">
            <div className="metric-card bad">
              <span>Legacy Complexity</span>
              <strong>{metrics.legacy_complexity}</strong>
            </div>
            <div className="metric-arrow">➔</div>
            <div className="metric-card good">
              <span>Modern Complexity</span>
              <strong>{metrics.modern_complexity}</strong>
            </div>
            <div className="metric-badge">
              {metrics.improvement} Cleaner
            </div>
          </div>
        )}
      </div>

      <div className="dashboard-grid">
        <div className="panel">
          <h3>Legacy Source (Cyclomatic: {metrics?.legacy_complexity || '-'})</h3>
          <textarea readOnly className="code-box legacy" value={legacyCode} />
          
          <h3>Generated Modern Source (Cyclomatic: {metrics?.modern_complexity || '-'})</h3>
          <textarea readOnly className="code-box modern" value={modernCode} />
        </div>

        <div className="panel">
          <h3>Agent Decision Logs</h3>
          <div className="terminal-window">
             {logs.map((l, i) => (
              <div key={i} className="log-entry" style={{
                // Color Logic:
                // Red if it says "FAILURE" or starts with "  [x]" (our new error detail)
                // Green if it says "SUCCESS"
                color: (l.includes("FAILURE") || l.includes("[x]")) ? '#ff7b72' : 
                       l.includes("SUCCESS") ? '#7ee787' : '#c9d1d9',
                // Add a little padding to indented errors
                paddingLeft: l.includes("[x]") ? '20px' : '8px' 
              }}>
                {l}
              </div>
            ))}
          </div>

          <h3>Final Verification</h3>
          <table className="results-table">
            <thead>
              <tr><th>Input</th><th>Legacy</th><th>Modern</th><th>Status</th></tr>
            </thead>
            <tbody>
              {testResults.map((r, i) => (
                <tr key={i}>
                  <td>{JSON.stringify(r.input_data)}</td>
                  <td>{r.legacy_output}</td>
                  <td>{r.modern_output}</td>
                  <td className={r.match ? "status-pass" : "status-fail"}>{r.match ? "MATCH" : "FAIL"}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
export default App