(async () => {
  let lastRan = Date.now();
  while (1) {
    if (Date.now() - lastRan > 2000) {
      console.log("was blocked for", Date.now() - lastRan, "ms");
    }
    lastRan = Date.now();
    await new Promise((resolve) => setTimeout(resolve, 1000));
  }
})();
