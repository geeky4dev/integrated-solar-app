import React from 'react';

const apps = [
  { name: 'Solar AI Designer', url: 'https://solar-ai-designer-frontend.onrender.com' },
  { name: 'Radiation Dashboard', url: 'https://solar-dashboard-1.onrender.com' },
  { name: 'Solar Optimizer', url: 'https://solar-orientation-tilt-app.onrender.com' },
  { name: 'Solar Savings Calculator', url: 'https://solar-savings-app-frontend.onrender.com' },
];

function App() {
  return (
    <div className="container mt-4">
      <h1 className="mb-4">🌞 Intergrated Solar App</h1>
      <div className="row">
        {apps.map((app, index) => (
          <div key={index} className="col-md-6 mb-4">
            <div className="card">
              <div className="card-header">{app.name}</div>
              <div className="card-body" style={{ height: '500px' }}>
                <iframe
                  src={app.url}
                  title={app.name}
                  style={{ border: 'none', width: '100%', height: '100%' }}
                ></iframe>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;

