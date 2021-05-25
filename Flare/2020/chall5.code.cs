using System;
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Security.Cryptography;
using System.Xml.Serialization;
using System.Text;
using System.IO;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            String text = "the kind of challenges we are gonna make here";
            byte[] Key = SHA256.Create().ComputeHash(Encoding.ASCII.GetBytes(text));
            byte[] IV = Encoding.ASCII.GetBytes("NoSaltOfTheEarth");
			byte[] cipherText = File.ReadAllBytes("C:\\Users\\IEUser\\Desktop\\Runtime.dll");

			string result = null;
			using (RijndaelManaged rijndaelManaged = new RijndaelManaged())
			{
				rijndaelManaged.Key = Key;
				rijndaelManaged.IV = IV;
				ICryptoTransform cryptoTransform = rijndaelManaged.CreateDecryptor(rijndaelManaged.Key, rijndaelManaged.IV);
				using (MemoryStream memoryStream = new MemoryStream(cipherText))
				{
					using (CryptoStream cryptoStream = new CryptoStream(memoryStream, cryptoTransform, 0))
					{
						using (StreamReader streamReader = new StreamReader(cryptoStream))
						{
							result = streamReader.ReadToEnd();
	
						}
					}
				}
			}
			byte[] newBytes = Convert.FromBase64String(result);

			using (var stream = new FileStream("test.jpg", FileMode.Create, FileAccess.Write, FileShare.None))
			using (var writer = new BinaryWriter(stream))
			{
				foreach (byte item in newBytes)
				{
					writer.Write(item);
				}
			}
			int temp;
			temp = 1;
		}
    }
}
