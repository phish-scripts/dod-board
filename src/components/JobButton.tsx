"use client";
import React from "react";

interface JobButtonProps {
  link: string;
}

const JobButton = ({ link }: JobButtonProps) => {
  return (
    <>
      <a className="btn btn-primary" href={link}>
        Apply
      </a>
    </>
  );
};

export default JobButton;
