using Microsoft.AspNetCore.Mvc;
using PortalEPI.Services;

namespace PortalEPI.Controllers
{
    public class EventsController : Controller
    {
        private readonly EventService _service;

        public EventsController(EventService service)
        {
            _service = service;
        }

        public async Task<IActionResult> Index()
        {
            var data = await _service.GetAllAsync();
            return View(data);
        }
    }
}
