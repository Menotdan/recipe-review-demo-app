using backend.Models;
using Microsoft.EntityFrameworkCore;

namespace backend.Db;

public class ReviewListContext(DbContextOptions options) : DbContext(options)
{
    public DbSet<ReviewModel> Reviews => Set<ReviewModel>();
}
