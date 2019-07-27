using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AngleSharp.Dom;
using AngleSharp.Text;

namespace NewsArticleWebScraper
{
    class Results
    {
        public void PrintResultsToResultsTextbox(string term, IEnumerable<IElement> storyLink)
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

        public void SaveResultsForWeeklyEmail(string term, IEnumerable<IElement> storyLink)
        {
            throw new NotImplementedException();
        }
    }
}
