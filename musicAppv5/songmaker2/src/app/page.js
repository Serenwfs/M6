
import React from 'react';
import Link from 'next/link';

const Page = () => {
  return (
    <div className="bg-pink-100 text-black h-screen flex flex-col items-center justify-center text-center p-4">
      <h1 className="text-4xl font-bold mb-2 protest-guerrilla">Song Maker</h1>
      <p className="text-xl mb-6">find inspiration through others</p>
      {/* <Link href="/search"  legacyBehavior>
        <a className="bg-red-500 text-white py-2 px-4 rounded-full hover:bg-red-700 transition-colors mb-4">Search through our songs...</a>
      </Link> */}
      <div className="space-x-4">
        <Link href="/Login"  legacyBehavior>
          <a className="bg-red-500 text-black py-2 px-4 rounded-full hover:bg-red-700 transition-colors">Log in</a>
        </Link>
        <Link href="/Register" legacyBehavior>
          <a className="bg-red-500 text-black py-2 px-4 rounded-full hover:bg-red-700 transition-colors">Sign in</a>
        </Link>
      </div>
    </div>
  );
};

export default Page;

// export default Page;


