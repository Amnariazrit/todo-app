// app/page.tsx
// Landing page with professional and responsive design

import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { ThemeToggle } from '@/components/theme/ThemeToggle';

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-cyan-50 dark:from-gray-900 dark:via-gray-800 dark:to-indigo-900">
      {/* Header */}
      <header className="sticky top-0 z-10 bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm border-b border-gray-200 dark:border-gray-800">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <nav className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <div className="w-10 h-10 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 flex items-center justify-center">
                <span className="text-white font-bold text-xl">T</span>
              </div>
              <span className="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-cyan-500 bg-clip-text text-transparent">
                TaskFlow
              </span>
            </div>

            <div className="hidden md:flex items-center space-x-4">
              <Button variant="ghost" asChild>
                <Link href="/login">Login</Link>
              </Button>
              <Button variant="gradient" asChild>
                <Link href="/signup">Get Started</Link>
              </Button>
              <ThemeToggle />
            </div>

            {/* Mobile menu button */}
            <div className="md:hidden flex items-center space-x-2">
              <ThemeToggle />
              <button className="p-2 rounded-md text-gray-700 dark:text-gray-300">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              </button>
            </div>
          </nav>
        </div>
      </header>

      {/* Hero Section */}
      <main className="flex-grow">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-24">
          <div className="max-w-7xl mx-auto">
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
              <div className="text-center lg:text-left">
                <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold tracking-tight">
                  <span className="block">Elevate Your</span>
                  <span className="block bg-gradient-to-r from-indigo-500 via-purple-500 to-cyan-500 bg-clip-text text-transparent mt-2">
                    Productivity
                  </span>
                </h1>

                <p className="mt-6 text-lg text-gray-600 dark:text-gray-300 max-w-2xl mx-auto lg:mx-0">
                  Experience the most beautiful and intuitive task management system.
                  Designed for efficiency and elegance, helping you accomplish more with less effort.
                </p>

                <div className="mt-10 flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
                  <Button size="lg" variant="gradient" className="px-8 py-4 text-lg" asChild>
                    <Link href="/signup">Start Free Trial</Link>
                  </Button>
                  <Button size="lg" variant="outline" className="px-8 py-4 text-lg" asChild>
                    <Link href="/login">Sign In</Link>
                  </Button>
                </div>

                <div className="mt-12 grid grid-cols-3 gap-8 max-w-xs mx-auto lg:mx-0">
                  <div className="text-center">
                    <div className="text-3xl font-bold text-indigo-600 dark:text-indigo-400">10K+</div>
                    <div className="text-sm text-gray-600 dark:text-gray-400">Tasks Managed</div>
                  </div>
                  <div className="text-center">
                    <div className="text-3xl font-bold text-purple-600 dark:text-purple-400">99%</div>
                    <div className="text-sm text-gray-600 dark:text-gray-400">Uptime</div>
                  </div>
                  <div className="text-center">
                    <div className="text-3xl font-bold text-cyan-600 dark:text-cyan-400">24/7</div>
                    <div className="text-sm text-gray-600 dark:text-gray-400">Support</div>
                  </div>
                </div>
              </div>

              <div className="relative">
                <div className="relative aspect-video bg-gradient-to-br from-indigo-100 to-cyan-100 dark:from-gray-800 dark:to-gray-700 rounded-2xl shadow-xl overflow-hidden border border-white/30 dark:border-gray-700/50">
                  <div className="absolute inset-0 flex items-center justify-center p-8">
                    <div className="w-full max-w-md bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-xl shadow-lg p-6 border border-white/30 dark:border-gray-700/30">
                      <div className="flex justify-between items-center mb-6">
                        <h3 className="font-bold text-lg">Today's Tasks</h3>
                        <div className="w-3 h-3 rounded-full bg-red-500"></div>
                      </div>

                      <div className="space-y-4">
                        <div className="flex items-center p-3 bg-white/50 dark:bg-gray-700/50 backdrop-blur-sm rounded-lg border border-white/30 dark:border-gray-600/30">
                          <div className="w-5 h-5 rounded border border-gray-300 mr-3"></div>
                          <span>Complete project proposal</span>
                          <span className="ml-auto bg-red-100 text-red-800 text-xs px-2 py-1 rounded-full">High</span>
                        </div>

                        <div className="flex items-center p-3 bg-white/50 dark:bg-gray-700/50 backdrop-blur-sm rounded-lg border border-white/30 dark:border-gray-600/30">
                          <div className="w-5 h-5 rounded border border-gray-300 mr-3"></div>
                          <span>Team meeting at 3 PM</span>
                          <span className="ml-auto bg-yellow-100 text-yellow-800 text-xs px-2 py-1 rounded-full">Medium</span>
                        </div>

                        <div className="flex items-center p-3 bg-white/50 dark:bg-gray-700/50 backdrop-blur-sm rounded-lg border border-white/30 dark:border-gray-600/30">
                          <div className="w-5 h-5 rounded-full bg-green-500 mr-3"></div>
                          <span className="line-through text-gray-400">Buy groceries</span>
                          <span className="ml-auto bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full">Low</span>
                        </div>
                      </div>

                      <div className="mt-6 pt-4 border-t border-gray-200 dark:border-gray-700 flex">
                        <input
                          type="text"
                          placeholder="Add a new task..."
                          className="flex-1 bg-white/70 dark:bg-gray-700/70 backdrop-blur-sm rounded-l-lg px-4 py-2 focus:outline-none border border-white/30 dark:border-gray-600/30"
                        />
                        <button className="bg-gradient-to-r from-indigo-500 to-cyan-500 text-white px-4 rounded-r-lg">
                          +
                        </button>
                      </div>
                    </div>
                  </div>

                  {/* Decorative elements */}
                  <div className="absolute -top-6 -right-6 w-24 h-24 rounded-full bg-purple-200 dark:bg-purple-900/30 opacity-50 blur-xl"></div>
                  <div className="absolute -bottom-8 -left-8 w-32 h-32 rounded-full bg-cyan-200 dark:bg-cyan-900/30 opacity-50 blur-xl"></div>
                </div>

                {/* Floating elements */}
                <div className="absolute -top-4 -left-4 w-20 h-20 rounded-xl bg-gradient-to-r from-indigo-400 to-purple-400 shadow-lg"></div>
                <div className="absolute -bottom-4 -right-4 w-16 h-16 rounded-lg bg-gradient-to-r from-cyan-400 to-blue-400 shadow-lg"></div>
              </div>
            </div>

            {/* Features Section */}
            <div className="mt-32">
              <h2 className="text-3xl font-bold text-center mb-16">Why Choose TaskFlow?</h2>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm p-8 rounded-2xl shadow-lg border border-white/30 dark:border-gray-700/30 transition-transform duration-300 hover:scale-105">
                  <div className="w-14 h-14 rounded-xl bg-indigo-100 dark:bg-indigo-900/30 flex items-center justify-center mb-6">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                  </div>
                  <h3 className="text-xl font-bold mb-3">Lightning Fast</h3>
                  <p className="text-gray-600 dark:text-gray-400">
                    Our optimized platform ensures tasks are synced instantly across all your devices.
                  </p>
                </div>

                <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm p-8 rounded-2xl shadow-lg border border-white/30 dark:border-gray-700/30 transition-transform duration-300 hover:scale-105">
                  <div className="w-14 h-14 rounded-xl bg-cyan-100 dark:bg-cyan-900/30 flex items-center justify-center mb-6">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8 text-cyan-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                    </svg>
                  </div>
                  <h3 className="text-xl font-bold mb-3">Secure & Private</h3>
                  <p className="text-gray-600 dark:text-gray-400">
                    Military-grade encryption keeps your tasks and data safe from unauthorized access.
                  </p>
                </div>

                <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm p-8 rounded-2xl shadow-lg border border-white/30 dark:border-gray-700/30 transition-transform duration-300 hover:scale-105">
                  <div className="w-14 h-14 rounded-xl bg-purple-100 dark:bg-purple-900/30 flex items-center justify-center mb-6">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8 text-purple-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                    </svg>
                  </div>
                  <h3 className="text-xl font-bold mb-3">Team Collaboration</h3>
                  <p className="text-gray-600 dark:text-gray-400">
                    Share tasks, assign responsibilities, and collaborate in real-time with your team.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm border-t border-gray-200 dark:border-gray-800">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-2 mb-4">
                <div className="w-8 h-8 rounded-lg bg-gradient-to-r from-indigo-500 to-cyan-500 flex items-center justify-center">
                  <span className="text-white font-bold">T</span>
                </div>
                <span className="text-xl font-bold">TaskFlow</span>
              </div>
              <p className="text-gray-600 dark:text-gray-400">
                The most intuitive task management solution for individuals and teams.
              </p>
            </div>

            <div>
              <h4 className="font-bold text-lg mb-4">Product</h4>
              <ul className="space-y-2">
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Features</a></li>
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Pricing</a></li>
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Integrations</a></li>
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Roadmap</a></li>
              </ul>
            </div>

            <div>
              <h4 className="font-bold text-lg mb-4">Resources</h4>
              <ul className="space-y-2">
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Documentation</a></li>
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Tutorials</a></li>
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Blog</a></li>
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Support</a></li>
              </ul>
            </div>

            <div>
              <h4 className="font-bold text-lg mb-4">Company</h4>
              <ul className="space-y-2">
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">About Us</a></li>
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Careers</a></li>
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Contact</a></li>
                <li><a href="#" className="text-gray-600 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors">Partners</a></li>
              </ul>
            </div>
          </div>

          <div className="mt-12 pt-8 border-t border-gray-200 dark:border-gray-800 flex flex-col md:flex-row justify-between items-center">
            <p className="text-gray-600 dark:text-gray-400 mb-4 md:mb-0">
              © {new Date().getFullYear()} TaskFlow. All rights reserved.
            </p>
            <div className="flex space-x-4">
              <ThemeToggle />
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}