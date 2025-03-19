import axios from 'axios';

const API_URL = 'http://localhost:5000';

export const predictImage = async (file) => {
  const formData = new FormData();
  formData.append('file', file);
  const response = await axios.post(`${API_URL}/predict`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
  return response.data;
};
