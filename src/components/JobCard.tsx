/* phish.dev
  02/11/26
  This react components purpose is to be populated 
  with Job data from Supabase, and then populate the job-board page with itself.
*/

import React from "react";

interface Job {
  job_url: string;
  job_title: string;
  location?: string[];
  salary?: string;
  remote_status?: string;
  pay_scale_grade?: string;
  description?: string;
}

interface JobCardProps {
  jobData: Job;
}

const JobCard = ({ jobData }: JobCardProps) => {
  return (
    <>
      <div className="card card-border bg-base-100 w-96">
        <div className="card-body">
          // Job Title
          <h2 className="card-title">{jobData.job_title}</h2>
          // Job Description
          <p>Sample Job text.</p>
          <div className="card-actions justify-end">
            // Job Url attatched to the button
            <a
              href={jobData.job_url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-block"
            >
              <button className="btn btn-primary">Apply Now</button>
            </a>
          </div>
        </div>
      </div>
    </>
  );
};

export default JobCard;
