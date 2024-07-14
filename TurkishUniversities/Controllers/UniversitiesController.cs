using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using TurkishUniversities.Data;
using TurkishUniversities.Models;

namespace TurkishUniversities.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UniversitiesController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public UniversitiesController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<Universities>>> GetUniversities()
        {
            return await _context.Universities.ToListAsync();
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Universities>> GetUniversities(Guid id)
        {
            var university = await _context.Universities.FindAsync(id);

            if (university == null)
            {
                return NotFound();
            }

            return university;
        }

        [HttpPost]
        public async Task<ActionResult<Universities>> PostUniversities(Universities university)
        {
            _context.Universities.Add(university);
            await _context.SaveChangesAsync();

            return CreatedAtAction(nameof(GetUniversities), new { id = university.ID }, university);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> PutUniversities(Guid id, Universities university)
        {
            if (id != university.ID)
            {
                return BadRequest();
            }

            _context.Entry(university).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!_context.Universities.Any(u => u.ID == id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteUniversities(Guid id)
        {
            var university = await _context.Universities.FindAsync(id);
            if (university == null)
            {
                return NotFound();
            }

            _context.Universities.Remove(university);
            await _context.SaveChangesAsync();

            return NoContent();
        }
    }

}
