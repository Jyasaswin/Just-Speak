"use client";

import Editor from "@monaco-editor/react";

export default function Home() {
return ( <div className="h-screen p-6"> <Editor
     height="90vh"
     defaultLanguage="cpp"
     defaultValue="// Voice2Code"
   /> </div>
);
}
