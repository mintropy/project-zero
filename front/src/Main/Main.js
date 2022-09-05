import React from "react";
import MainAccountInfo from "./MainAccountInfo";
import MainBlogList from "./MainBlogList";

const Main = () => {
  return (
    <div className="Main">
      <h1>Main Page</h1>
      <MainBlogList />
      <MainAccountInfo />
    </div>
  );
};

export default Main;
