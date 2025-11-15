using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace PortalEPI.Models
{
    public class EventRecord
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }

        [BsonElement("date")]
        public DateTime Date { get; set; }

        [BsonElement("confidence")]
        public double Confidence { get; set; }

        [BsonElement("device")]
        public string Device { get; set; }
    }
}
