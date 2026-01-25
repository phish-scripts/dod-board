import { supabase } from "../supabaseSchema/supabaseObject";

export default function Home() {
  const m = async () => {
    await supabase.from("applications").select("*");
  };
  console.log("hello world");
  return console.log(m);
}
