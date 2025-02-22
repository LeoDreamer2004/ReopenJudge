import axiosInstance from './index'

const axios = axiosInstance

export const getProblems = () => { return axios.get(`http://127.0.0.1:8000/api/problems/`) }

export const postProblem = (title, description, difficulty) => {
  return axios.post(`http://127.0.0.1:8000/api/problems/`, {
    title: title,
    description: description,
    difficulty: difficulty
  })
}
