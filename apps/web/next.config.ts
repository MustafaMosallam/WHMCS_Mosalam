import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "export",
  trailingSlash: true,
  basePath: "/WHMCS_Mosalam",
  images: { unoptimized: true },
};

export default nextConfig;
