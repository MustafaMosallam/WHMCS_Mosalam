import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata={title:"Mosalam | Hosting & Cloud Infrastructure",description:"Hosting, VPS, VDS and cloud infrastructure for websites, applications and software teams."};
export default function RootLayout({children}:{children:React.ReactNode}){return <html lang="en"><body>{children}</body></html>}
