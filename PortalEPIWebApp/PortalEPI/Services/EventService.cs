using MongoDB.Driver;
using PortalEPI.Models;

namespace PortalEPI.Services
{
    public class EventService
    {
        private readonly IMongoCollection<EventRecord> _collection;

        public EventService(IConfiguration config)
        {
            var client = new MongoClient(config["MongoDB:ConnectionString"]);
            var database = client.GetDatabase(config["MongoDB:Database"]);
            _collection = database.GetCollection<EventRecord>(config["MongoDB:Collection"]);
        }

        public async Task<List<EventRecord>> GetAllAsync()
        {
            return await _collection.Find(_ => true).ToListAsync();
        }
    }
}
