// phish.dev
// this is the main page where all the jobs will be posted

import { supabase } from "../supabaseSchema/supabaseObject";
import JobCard from "@/components/JobCard";

const sampleJobs = [
  { id: 1, job_title: "Frontend Engineer", job_url: "https://google.com" },
  { id: 2, job_title: "Backend Developer", job_url: "https://github.com" },
  { id: 3, job_title: "UI Designer", job_url: "https://daisyui.com" },
];

export default function Home() {
  <>
    return (
    <main className="min-h-screen p-8 flex flex-col items-center bg-base-200">
      <h1 className="text-4xl font-black mb-10 uppercase italic">
        Job Scraper Feed
      </h1>

      {/* The Container for your "Stacked Boxes" */}
      <div className="flex flex-col gap-6 w-full max-w-2xl">
        {sampleJobs.map((job) => (
          <JobCard key={job.id} jobData={job} />
        ))}
      </div>
    </main>
    )
  </>;
}
