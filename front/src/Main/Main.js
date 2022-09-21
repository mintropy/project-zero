import React from "react";
import MainAccountInfo from "./MainAccountInfo";
import MainBlogList from "./MainBlogList";
import "./Main.css";

const Main = () => {
  return (
    <div className="Main">
      <MainBlogList />
      <MainAccountInfo />
    </div>
  );
};

export default Main;
