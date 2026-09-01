import http from 'k6/http';

export const options = {
  vus: 1,
  duration: '10s',
};

export default function () {
  http.get('http://127.0.0.1:8000/');
}