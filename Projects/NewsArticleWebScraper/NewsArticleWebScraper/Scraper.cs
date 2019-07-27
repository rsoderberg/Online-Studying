using System;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.Configuration;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading;
using AngleSharp.Dom;
using AngleSharp.Html.Dom;
using AngleSharp.Html.Parser;

namespace NewsArticleWebScraper
{
    class Scraper
    {
        private string[] queryTerms = {
            "Intro", "Tutorial", "Education", "Learn",
            "C#", "CSharp", "Neural", "IoT", "Simulation",
            "Green", "Animal", "Hagfish", "Nature",
            "Communication", "Language", "Translation", "French", "Français"
        };

        internal readonly NameValueCollection _appSettings = ConfigurationManager.AppSettings;

        public async void ScrapeHackerRank()
        {
            CancellationTokenSource cancellationToken = new CancellationTokenSource();
            HttpClient httpClient = new HttpClient();
            HttpResponseMessage request = await httpClient.GetAsync(_appSettings["HackerRankUrl"]);
            cancellationToken.Token.ThrowIfCancellationRequested();

            Stream response = await request.Content.ReadAsStreamAsync();
            cancellationToken.Token.ThrowIfCancellationRequested();

            HtmlParser parser = new HtmlParser();
            IHtmlDocument document = parser.ParseDocument(response);

            GetScrapeResults(queryTerms, document);
        }

        private void GetScrapeResults(string[] queryTerms, IHtmlDocument document)
        {
            IEnumerable<IElement> storyLink;
            foreach (var term in queryTerms)
            {
                storyLink = document.All.Where(x => x.ClassName == "storylink" && (x.InnerHtml.Contains(term) || x.InnerHtml.Contains(term.ToLower())));

                if (storyLink.Any())
                {
                    Results results = new Results();
                    results.PrintResultsToResultsTextbox(term, storyLink);
                    //results.SaveResultsForWeeklyEmail(term, storyLink);
                }
            }
        }
    }
}