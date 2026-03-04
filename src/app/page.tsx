// phish.dev
// this is the main page where all the jobs will be posted

import { supabase } from "../supabaseSchema/supabaseObject";
import JobPosting from "@/components/JobPosting";

/* 
    job_link: string;
    job_title: string;
    location?: string[];
    remote_status: string;
    pay_scale_grade: string;
    description: string;
    date_posted: string;
*/

export default function Home() {
  return (
    <>
      <JobPosting
        job_link=""
        job_title=""
        remote_status=""
        pay_scale_grade=""
        description=""
        date_posted=""
      />
    </>
  );
}
