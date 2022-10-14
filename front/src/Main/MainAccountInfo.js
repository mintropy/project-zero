import axios from "axios";
import React from "react";
import "./Main.css";
import getRefreshToken from "../JWTHandler.js";

const MainAccountInfo = ({ userInfo, setUserInfo, isLogin, toggleLogin }) => {
  const handleChange = (e) => {
    setUserInfo({
      ...userInfo,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios({
      method: "post",
      url: "http://127.0.0.1:8000/api/token/",
      data: userInfo,
    })
      .then((res) => {
        const access = res.data.access;
        const refresh = res.data.refresh;
        window.localStorage.setItem("access", access);
        window.localStorage.setItem("refresh", refresh);
        return access;
      })
      .then((access) => {
        const username = getUserInfo(access);
        toggleLogin();
        return username;
      });
    return res;
  };

  const getUserInfo = async (access) => {
    axios.defaults.headers.common["Authorization"] = `Bearer ${access}`;
    const res = await axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/users/profile/",
    }).then((res) => {
      const username = res.data.username;
      window.localStorage.setItem("username", username);
      return username;
    });
    return res;
  };

  return (
    <div className="MainAccountInfo">
      <h1>회원 관리</h1>
      {isLogin ? (
        <div>{userInfo.username} 님</div>
      ) : (
        <form onSubmit={handleSubmit}>
          <input
            name="username"
            value={userInfo.username}
            onChange={handleChange}
          />
          <br />
          <input
            name="password"
            type="password"
            value={userInfo.password}
            onChange={handleChange}
          />
          <br />
          <button type="submit">login</button>
        </form>
      )}
    </div>
  );
};

export default MainAccountInfo;
