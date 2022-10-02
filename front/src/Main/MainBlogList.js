import React, { useEffect, useState } from "react";
import axios from "axios";
import "./Main.css";

const MainBlogList = () => {
  const [blogs, setBlogs] = useState([]);
  const getBlogs = async () => {
    const res = await axios({
      method: "get",
      url: "http://127.0.0.1:8000/api/blogs/blog/",
    }).then((res) => res.data);
    setBlogs(res);
  };
  useEffect(() => {
    getBlogs();
  }, []);

  return (
    <div className="MainBlogList">
      <h1>블로그 목록</h1>
      <ul>
        {blogs.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default MainBlogList;
