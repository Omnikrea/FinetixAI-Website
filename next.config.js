/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',  // Enables static site generation (SSG)
  images: {
    unoptimized: true, // Ensures Cloudflare handles images properly
  },
};

module.exports = nextConfig;


