import React, { useEffect, useState } from "react";
import MainAccountInfo from "./MainAccountInfo";
import MainBlogList from "./MainBlogList";
import "./Main.css";

const Main = ({ isLogin, toggleLogin }) => {
  const [userInfo, setUserInfo] = useState({
    username: "",
    password: "",
  });

  return (
    <div className="Main">
      <MainBlogList />
      <MainAccountInfo
        userInfo={userInfo}
        setUserInfo={setUserInfo}
        isLogin={isLogin}
        toggleLogin={toggleLogin}
      />
    </div>
  );
};

export default Main;
