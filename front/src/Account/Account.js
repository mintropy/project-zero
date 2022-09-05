import React from "react";
import LoginForm from "./LoginForm";
import SignupForm from "./SignupForm";
import UserProfile from "./UserProfile";

const Account = () => {
  return (
    <div className="Account">
      <h1>회원 관련 페이지</h1>
      <LoginForm />
      <SignupForm />
      <UserProfile />
    </div>
  );
};

export default Account;
