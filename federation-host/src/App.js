import React from "react";

const App = () => {
  const App1 = React.lazy(() => import("telephony/TelephonyApp"));
  const App2 = React.lazy(() => import("internet/InternetApp"));

  return (
    <React.Suspense fallback="Loading...">
      <div>
        <h1>Federation Host</h1>
        <h2>Telephony Catalog</h2>
        <App1 />
        <h2>Internet Catalog</h2>
        <App2 />
      </div>
    </React.Suspense>
  );
};

export default App;
