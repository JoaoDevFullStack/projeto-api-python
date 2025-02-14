using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ImportCSVAPI.Data;
using ImportCSVAPI.Models;
using System.IO;
using System.Threading.Tasks;
using System.Collections.Generic;

namespace ImportCSVAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PessoaController : ControllerBase
    {
        private readonly AppDbContext _context;

        public PessoaController(AppDbContext context)
        {
            _context = context;
        }

        [HttpPost("importar")]
        public async Task<IActionResult> ImportCSV(IFormFile file)
        {
            if (file == null || file.Length == 0)
                return BadRequest("Nenhum arquivo selecionado.");

            var pessoas = new List<Pessoa>();

            // Criando o StreamReader corretamente
            using (var stream = new StreamReader(file.OpenReadStream()))
            {
                string line;
#pragma warning disable CS8600 // Converting null literal or possible null value to non-nullable type.
                while ((line = await stream.ReadLineAsync()) != null)
                {
                    var values = line.Split(',');

                    // Ignorar a primeira linha (cabeçalho)
                    if (values[0] == "Id")
                        continue;

                    var pessoa = new Pessoa
                    {
                        Nome = values[1],
                        Idade = int.Parse(values[2]),
                        Cidade = values[3],
                        Profissao = values[4]
                    };

                    pessoas.Add(pessoa);
                }
#pragma warning restore CS8600 // Converting null literal or possible null value to non-nullable type.
            }

            await _context.Pessoas.AddRangeAsync(pessoas);
            await _context.SaveChangesAsync();

            return Ok(new { Message = "Arquivo CSV importado com sucesso!" });
        }
        [HttpGet("{id}")]
public async Task<IActionResult> GetPessoa(int id)
{
    var pessoa = await _context.Pessoas.FindAsync(id);

    if (pessoa == null)
        return NotFound();

    return Ok(pessoa);
}
        
    }
}
