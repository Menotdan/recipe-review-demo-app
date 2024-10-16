using Microsoft.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;

namespace backend.Models;

[PrimaryKey(nameof(Id))]
public class ReviewModel
{
    public int Id { get; set; }

    [MaxLength(50, ErrorMessage = "Name too long!")]
    public string Name { get; set; } = string.Empty;

    [MaxLength(2000, ErrorMessage = "Text too long!")]
    public string Text { get; set; } = string.Empty;

    [Range(0, 10)]
    public int Rating { get; set; }

    [Range(0, int.MaxValue)]
    public int Likes { get; set; }

    public ReviewModel() { }

    public ReviewModel(ReviewPostModel postedReview)
    {
        Name = postedReview.Name;
        Text = postedReview.Text;
        Rating = postedReview.Rating;
    }
}

public class ReviewPostModel
{

    [MaxLength(50, ErrorMessage = "Name too long!"), Required]
    public string Name { get; set; } = string.Empty;

    [MaxLength(2000, ErrorMessage = "Text too long!"), Required]
    public string Text { get; set; } = string.Empty;

    [Range(0, 10), Required]
    public int Rating { get; set; }
}