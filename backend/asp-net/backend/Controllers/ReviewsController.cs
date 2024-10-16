using backend.Db;
using backend.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Net.Http;

namespace backend.Controllers;

[ApiController]
[Route("/api/[controller]")]
public class ReviewsController : ControllerBase
{
    private readonly ILogger<ReviewsController> _logger;
    private ReviewListContext? _dbContext => HttpContext.RequestServices.GetService<ReviewListContext>();

    public ReviewsController(ILogger<ReviewsController> logger)
    {
        _logger = logger;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<ReviewModel>>> GetAllReviews()
    {
        if (_dbContext == null)
            return Problem(detail: "Database missing.");

        return Ok(await _dbContext.Reviews.ToListAsync());
    }

    [HttpPost, Route("like/{id:int}")]
    public async Task<ActionResult<ReviewModel>> PostReviewLike(int id)
    {
        if (_dbContext == null)
            return Problem(detail: "Database missing.");

        ReviewModel? review = await _dbContext.FindAsync<ReviewModel>(id);

        if (review == null)
            return NotFound();

        review.Likes += 1;
        _dbContext.Update(review);
        _ = await _dbContext.SaveChangesAsync();

        return review;
    }

    [HttpPost, Route("create")]
    public async Task<ActionResult<int>> PostReview(ReviewPostModel postingReview)
    {
        if (_dbContext == null)
            return Problem(detail: "Database missing.");

        ReviewModel postedReview = new ReviewModel(postingReview);

        _dbContext.Add(postedReview);
        _ = await _dbContext.SaveChangesAsync();

        return Ok(postedReview.Id);
    }
}