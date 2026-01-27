'use server'

import { createClient } from "../../../supabaseClientServer/supabase_client"
import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";

export async function login(formData: FormData)
{
    const supabase = await createClient();

    const email = formData.get('email') as string;
    const password = formData.get('password') as string;

    const { error } = await supabase.auth.signInWithPassword({ email, password});

    if (error)
    {
        return redirect("/login?message=Invalid Credentials!");

    }

    revalidatePath('/', 'layout')
    redirect('/dashboard')
  
}

