import axios from "axios";

const getRefreshToken = async () => {
  const refresh = window.localStorage.getItem("refresh");

  const res = await axios({
    method: "post",
    url: "http://127.0.0.1:8000/api/token/refresh/",
    data: { refresh: refresh },
  }).then((res) => {
    const access = res.data.access;
    window.localStorage.setItem("access", access);
  });
};

export default getRefreshToken;
