"use server";
import React from "react";

/* 
    This component renders details about the Job Postings
*/

import JobButton from "./JobButton";

interface JobProps {
  job_link: string;
  job_title: string;
  // location: string[];
  remote_status: string;
  pay_scale_grade: string;
  description: string;
  date_posted: string;
}

const JobPosting = async ({
  job_link,
  job_title,
  // location,
  remote_status,
  pay_scale_grade,
  description,
  date_posted,
}: JobProps) => {
  return (
    <>
      <div className="card card-border bg-base-100 w-96">
        <div className="card-body">
          <h2 className="card-title">
            {job_title}
            <div className="badge badge-secondary">{pay_scale_grade}</div>
          </h2>
          <p>{description}</p>
          <div className="card-actions justify-end">
            <JobButton link={job_link} />
            <div className="badge badge-outline">{remote_status}</div>
            <div className="badge badge-outline">{date_posted}</div>
          </div>
        </div>
      </div>
    </>
  );
};

export default JobPosting;
