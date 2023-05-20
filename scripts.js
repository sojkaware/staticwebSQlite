document.addEventListener("DOMContentLoaded", function () {
    const vfs = SQL.HTTPVFS("reviews.db");
    const config = { vfs };
    const btnMovieReviews = document.getElementById("btnMovieReviews");
    const reviewsTable = document.getElementById("reviewsTable");
    const reviewsTableBody = document.getElementById("reviewsTableBody");
  
    btnMovieReviews.addEventListener("click", async function () {
      if (reviewsTable.classList.contains("hidden")) {
        reviewsTable.classList.remove("hidden");
        await loadMovieReviews();
      }
    });
  
    async function loadMovieReviews() {
      const db = await SQL(config);
      const result = await db.exec("SELECT * FROM movie_reviews");
      const movieReviews = result[0].values;
  
      movieReviews.forEach((review) => {
        const row = document.createElement("tr");
        review.forEach((cell) => {
          const td = document.createElement("td");
          td.textContent = cell;
          row.appendChild(td);
        });
        reviewsTableBody.appendChild(row);
      });
  
      await db.close();
    }
  });