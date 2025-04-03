// Load placeholder financial news when the page loads
document.addEventListener("DOMContentLoaded", () => {
  const newsFeed = document.getElementById("news-feed");

  // Placeholder example news articles
  const sampleNews = [
    {
      title: "AI Revolution in Stock Trading",
      snippet: "GPT-based advisors are transforming how investors make decisions."
    },
    {
      title: "Crypto Market Surges on Global Demand",
      snippet: "Bitcoin hits record highs as institutional interest grows."
    },
    {
      title: "FinetixAI Launches New Financial Tools",
      snippet: "Advanced budgeting and forecasting features rolling out this quarter."
    }
  ];

  // Render them into the page
  newsFeed.innerHTML = sampleNews
    .map((article) => {
      return `
        <div class="news-article">
          <h3>${article.title}</h3>
          <p>${article.snippet}</p>
        </div>
      `;
    })
    .join("");
});
