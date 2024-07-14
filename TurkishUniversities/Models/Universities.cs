namespace TurkishUniversities.Models
{
    public class Universities
    {
        public Guid ID { get; set; }
        public int CategoryID { get; set; }
        public string? DataOrder { get; set; }

        public string? Name { get; set; }

        public string? Website { get; set; }

        public string? Address { get; set; }
        public string? DetailsLink { get; set; }

        public string? ProgramsLink { get; set; }

        public string? ImageURL { get; set;}

        public string? LogoURL { get; set;}



    }
}
