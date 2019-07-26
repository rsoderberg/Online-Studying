namespace NewsArticleWebScraper
{
    partial class WebScraperForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.startButton = new System.Windows.Forms.Button();
            this.resultsTextbox = new System.Windows.Forms.RichTextBox();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.timerLabel = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // startButton
            // 
            this.startButton.Location = new System.Drawing.Point(258, 609);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(75, 23);
            this.startButton.TabIndex = 0;
            this.startButton.Text = "Start";
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // resultsTextbox
            // 
            this.resultsTextbox.Location = new System.Drawing.Point(12, 12);
            this.resultsTextbox.MaximumSize = new System.Drawing.Size(580, 591);
            this.resultsTextbox.MinimumSize = new System.Drawing.Size(580, 591);
            this.resultsTextbox.Name = "resultsTextbox";
            this.resultsTextbox.Size = new System.Drawing.Size(580, 591);
            this.resultsTextbox.TabIndex = 1;
            this.resultsTextbox.Text = "";
            // 
            // timer1
            // 
            this.timer1.Interval = 1000;
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // timerLabel
            // 
            this.timerLabel.AutoSize = true;
            this.timerLabel.Location = new System.Drawing.Point(581, 617);
            this.timerLabel.Name = "timerLabel";
            this.timerLabel.Size = new System.Drawing.Size(0, 13);
            this.timerLabel.TabIndex = 2;
            // 
            // WebScraperForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(604, 640);
            this.Controls.Add(this.timerLabel);
            this.Controls.Add(this.resultsTextbox);
            this.Controls.Add(this.startButton);
            this.MaximumSize = new System.Drawing.Size(620, 679);
            this.MinimumSize = new System.Drawing.Size(620, 679);
            this.Name = "WebScraperForm";
            this.Text = "WebScraper";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.RichTextBox resultsTextbox;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.Label timerLabel;
    }
}

