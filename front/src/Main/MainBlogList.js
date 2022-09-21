import React from "react";
import "./Main.css";

const MainBlogList = () => {
  fetch("http://127.0.0.1:8000/api/blogs/blog/").then((res) =>
    console.log(res)
  );

  return (
    <div className="MainBlogList">
      <h1>블로그 목록</h1>
    </div>
  );
};

export default MainBlogList;
