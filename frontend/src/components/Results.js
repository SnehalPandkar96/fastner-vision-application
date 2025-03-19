import React from 'react';

const Results = ({ detections }) => {
  return (
    <div>
      <h2>Detection Results</h2>
      <ul>
        {detections.map((det, index) => (
          <li key={index}>
            Class: {det.class} | Confidence: {(det.confidence * 100).toFixed(2)}% | BBox: {JSON.stringify(det.bbox)}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Results;
