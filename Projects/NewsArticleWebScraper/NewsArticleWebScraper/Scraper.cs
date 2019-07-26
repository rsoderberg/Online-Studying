using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading;
using AngleSharp.Html.Dom;
using AngleSharp.Html.Parser;
using AngleSharp.Text;

namespace NewsArticleWebScraper
{
    class Scraper
    {
        private string websiteUrl = "https://news.ycombinator.com/";

        private string[] queryTerms = {
            "Introduction", "Tutorial", "Education", "Learn",
            "C#", "Neural", "IoT", "Simulation",
            "Green", "Animal", "Hagfish",
            "Communication"

        };

        public async void scrapeWebsite()
        {
            CancellationTokenSource cancellationToken = new CancellationTokenSource();
            HttpClient httpClient = new HttpClient();
            HttpResponseMessage request = await httpClient.GetAsync(websiteUrl);
            cancellationToken.Token.ThrowIfCancellationRequested();

            Stream response = await request.Content.ReadAsStreamAsync();
            cancellationToken.Token.ThrowIfCancellationRequested();

            HtmlParser parser = new HtmlParser();
            IHtmlDocument document = parser.ParseDocument(response);

            IEnumerable<AngleSharp.Dom.IElement> storyLink;
            foreach (var term in queryTerms)
            {
                storyLink = document.All.Where(x => x.ClassName == "storylink" && (x.InnerHtml.Contains(term) || x.InnerHtml.Contains(term.ToLower())));

                if (storyLink.Any())
                {
                    foreach (var result in storyLink)
                    {
                        string htmlResult = result.OuterHtml.ReplaceFirst("<a href=\"", "");
                        htmlResult = htmlResult.ReplaceFirst("\" class=\"storylink\">", "*");
                        htmlResult = htmlResult.ReplaceFirst("</a>", "");

                        string[] splitResults = htmlResult.Split('*');
                        string url = splitResults[0];
                        string title = splitResults[1];

                        WebScraperForm.ProcessMonitor.UpdateTextBox($"{title} - {url}{Environment.NewLine}");
                    }

                    WebScraperForm.ProcessMonitor.UpdateTextBox($"-----{term}-----");
                }
            }
        }
    }
}