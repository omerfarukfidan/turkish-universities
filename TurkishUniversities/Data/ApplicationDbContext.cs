using Microsoft.EntityFrameworkCore;
using TurkishUniversities.Models;

namespace TurkishUniversities.Data
{
    public class ApplicationDbContext : DbContext
    {
        public DbSet<Universities> Universities { get; set;}

        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options) : base(options) { }

    }
}
