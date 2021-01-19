using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;

namespace app.Pages
{

    class ExpectedType {

    }
    
    public class PrivacyModel : PageModel
    {
        private readonly ILogger<PrivacyModel> _logger;

        public PrivacyModel(ILogger<PrivacyModel> logger)
        {
            _logger = logger;
        }

        public void OnGet()
        {
        }

        public void OnPost()
        {
            ViewData["error"] = String.Empty;
            var untrusted = Request.Form["json"];

            try {
                // pre v2.3.0
                var obj = (ExpectedType) fastJSON.JSON.ToObject(untrusted);
                // v2.3.0 onwards
                // var obj = (ExpectedType) fastJSON.JSON.ToObject(untrusted, new fastJSON.JSONParameters { BadListTypeChecking = false });
            } catch (Exception e) {
                ViewData["error"] = e.ToString();
            }
        }
    }
}
