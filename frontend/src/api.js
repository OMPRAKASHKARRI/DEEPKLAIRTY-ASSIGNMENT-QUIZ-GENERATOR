import axios from "axios";

const api = axios.create({
  baseURL: "https://deepklairty-assignment-quiz-generator.onrender.com/api",
});

export default api;
