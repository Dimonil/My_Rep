using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SQLite;
using System.Data.Sql;


namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public string getScalar(SQLiteConnection DB,string s,int id)
        {
            SQLiteCommand CMD = DB.CreateCommand();
            CMD.CommandText = s;
            CMD.Parameters.Add("@id", System.Data.DbType.Int32).Value = id;
            return CMD.ExecuteScalar().ToString();

        }
        public SQLiteDataReader getReader(SQLiteConnection DB, string s,int id)
        {
            
            SQLiteCommand CMD = DB.CreateCommand();
            CMD.CommandText = s;
            CMD.Parameters.Add("@date", System.Data.DbType.Date).Value = textDate.Text;
            CMD.Parameters.Add("@id", System.Data.DbType.Int16).Value = id;
            return CMD.ExecuteReader();

        }
        struct Money
        {
            public double all, first_lvl;
            public Money(double all, double first_lvl)
            {
                this.all = all;
                this.first_lvl = first_lvl;
            }
            public void Add(Money money)
            {
                this.all += money.all;
                this.first_lvl += money.first_lvl;

            }

        }
        private SQLiteConnection DB;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DB = new SQLiteConnection("Data source = DBTest.db");
            DB.Open();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            DB.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (textName.Text != "" && textGroup.Text != "")
            {
                SQLiteCommand CMD = DB.CreateCommand();
                CMD.CommandText = "select max(id) from staffs";
                var a = CMD.ExecuteScalar();
                //label3.Text = Convert.ToString(a);





                CMD.CommandText = "insert into staffs(id, name, date ,id_group)  values (@id + 1, @name,  Date('now') ,@group)";
                CMD.Parameters.Add("@id", System.Data.DbType.Int32).Value = a;
                CMD.Parameters.Add("@name", System.Data.DbType.String).Value = textName.Text.ToUpper();
                CMD.Parameters.Add("@group", System.Data.DbType.Int16).Value = Convert.ToInt16(textGroup.Text);

                CMD.ExecuteNonQuery();


            }
        }
        
        private void button1_Click(object sender, EventArgs e)
        {
            if (textDate.Text != "" && textId.Text != "")
            {
                SQLiteDataReader reader;             
                reader = getReader(DB, "select id,id_group from staffs where id in (@id)", Convert.ToInt16(textId.Text)); // Создание ридера подчинненых искомого 
                DateTime date = dateTimePicker1.Value;
                //
                {
                    SQLiteCommand CMD = DB.CreateCommand();
                    CMD.CommandText = "select date from staffs where id = 6";
                    DateTime a = (DateTime)CMD.ExecuteScalar();
                    MessageBox.Show(a.ToString());

                }





                ////
                label3.Text = date.ToString();
                //label5.Text = date.ToShortDateString();

                
                double money = Convert.ToInt32(getScalar(DB, "select base_rate from groups,staffs where staffs.id = @id and staffs.id_group = groups.id_group", Convert.ToInt16(textId.Text))); //поиск базовой зарплаты искомого

                SQLiteCommand newCMD = DB.CreateCommand();
                newCMD.Parameters.Add("@id", System.Data.DbType.Int32).Value = Convert.ToInt16(textId.Text);
                newCMD.CommandText = "select date from staffs where id = @id";
                DateTime dateId = (DateTime)newCMD.ExecuteScalar();// дата поиска зарплаты
                ///dateId = (DateTime)dateId;
                ///dateId = dateId + date;
                label4.Text = Convert.ToString(Zp(reader).first_lvl);


                 

                






            }


        }
        Money Zp(SQLiteDataReader reader)
        {
            Money count = new Money(0, 0);
            while (reader.Read())
            {

                SQLiteCommand CMD = DB.CreateCommand();
                CMD.Parameters.Add("@id", System.Data.DbType.Int32).Value = reader.GetInt32(0);

                CMD.CommandText = "select id,id_group from staffs where id_n in (@id)";

                SQLiteDataReader new_reader = CMD.ExecuteReader();
                if (new_reader.HasRows)
                {
                    count.Add(Zp(new_reader));
                    SQLiteCommand nCMD = DB.CreateCommand();
                    nCMD.Parameters.Add("@id", System.Data.DbType.Int32).Value = reader.GetInt32(0);
                    CMD.Parameters.Add("@date", System.Data.DbType.Date).Value = textDate.Text;
                    nCMD.CommandText = "select base_rate,groups.id_group from groups,staffs where staffs.id = @id and staffs.id_group = groups.id_group";
                    SQLiteDataReader new_reader1 = nCMD.ExecuteReader();

                    if (new_reader1.Read())
                    {
                        if (new_reader1.GetValue(1).ToString() == "1")
                        {
                            count.first_lvl += (double)new_reader1.GetValue(0);
                        }
                        if (new_reader1.GetValue(1).ToString() == "2")
                        {
                            count.all += count.first_lvl * 0.5;
                        }
                        if (new_reader1.GetValue(1).ToString() == "3")
                        {
                            count.all += count.all * 0.3;
                        }
                        count.all += Convert.ToInt32(new_reader1.GetValue(0));
                    }
                    

                    //label5.Text += "," + reader.GetValue(0).ToString();

                }
                else
                {
                    SQLiteCommand nCMD = DB.CreateCommand();
                    
                    nCMD.Parameters.Add("@id", System.Data.DbType.Int32).Value = reader.GetInt32(0);
                    nCMD.CommandText = "select base_rate,groups.id_group from groups,staffs where staffs.id = @id and staffs.id_group = groups.id_group";
                    SQLiteDataReader new_reader2 = nCMD.ExecuteReader();
                                       
                    if (new_reader2.Read())
                    {
                        if (new_reader2.GetValue(0).ToString() == "1")
                        {
                            count.first_lvl += (double)new_reader2.GetValue(0);
                        }
                        if (new_reader2.GetValue(1).ToString() == "2")
                        {
                            count.all += count.first_lvl * 0.5;
                        }
                        if (new_reader2.GetValue(1).ToString() == "3")
                        {
                            count.all += count.all * 0.3;
                        }
                        count.all += Convert.ToInt32(new_reader2.GetValue(0));
                    }
                    

                }

            }

           
            return count;
            



        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        { 
          
        }
    }
}
