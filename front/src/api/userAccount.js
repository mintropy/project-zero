import axios from "axios";

const getUserInfo = async () => {
  const access = localStorage.getItem("access");
  const res = await axios({
    method: "get",
    url: "http://127.0.0.1:8000/api/users/profile/",
  })
    .then((res) => {
      const username = res.data.username;
      return username;
    })
    .catch((err) => "");
  return res;
};

export { getUserInfo };
