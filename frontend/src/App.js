import React, { useState } from 'react';
import Upload from './components/Upload';
import Results from './components/Results';
import axios from 'axios';

function App() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (file) => {
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:5000/predict', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      setResults(response.data.detections);
    } catch (error) {
      console.error('Error during prediction:', error);
      alert('Error during prediction');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Object Detection Demo</h1>
      <Upload onUpload={handleUpload} loading={loading} />
      {results && <Results detections={results} />}
    </div>
  );
}

export default App;
