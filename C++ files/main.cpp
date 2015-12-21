#include <iostream>
#include "FinData.h"
#include <fstream>
#include <string>


extern const string		TABLES = "C:\\Users\\Public\\Documents\\Stephy files\\NJIT\\Fall 2015\\Project\\training\\tables.txt";

/// <summary>
/// Generate probability function tables for each table in the text file containing the list of table data paths. 
/// Note that you need the direct path to a textfile, which has a list of absolute paths to stock data tables.</summary>
void gen_Pdf() 
{
	//	create temporary string
	//	create input filestream
	//	read through each table in tablelist
	//		generate pdf for each table in the table list
	//	close input filestream


	string      tem;
	ifstream FSTREAM;
	FSTREAM.open(TABLES);
	while (getline(FSTREAM, tem, '\n'))
	{
		getPDFs(tem, 1);
	}
	FSTREAM.close();
}



int main()
{
	
	// Run pdf generation
	gen_Pdf();



	return 0;
}



