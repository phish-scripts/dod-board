import { type NextRequest } from "next/server"

// yes, i kknow the imports are a bit of a mess
import { updateSession } from "./supabaseClientServer/proxy"

export async function proxy(request: NextRequest) {

  return await updateSession(request)

}

export const config = {

  matcher: [

    /*

     * Match all request paths except for the ones starting with:

     * - _next/static (static files)

     * - _next/image (image optimization files)

     * - favicon.ico (favicon file)

     * Feel free to modify this pattern to include more paths.

     */

    "/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)",

  ],

}